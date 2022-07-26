package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"

	jwtmiddleware "github.com/auth0/go-jwt-middleware"
	"github.com/dgrijalva/jwt-go"
	"github.com/gorilla/mux"
)

var jwtSecret string = os.Getenv("APP_JWT_SECRET")

func GetUser(w http.ResponseWriter, req *http.Request) {
	user := req.Context().Value("user").(*jwt.Token)
	claims := user.Claims.(jwt.MapClaims)

	responseStruct := struct {
		UserID       interface{} `json:"user_id"`
		UserFullName interface{} `json:"user_full_name"`
		UserEmail    interface{} `json:"user_email"`
	}{
		UserID:       claims["user_id"],
		UserFullName: claims["user_full_name"],
		UserEmail:    claims["user_email"],
	}

	response, err := json.Marshal(responseStruct)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(err.Error()))
	} else {
		w.WriteHeader(http.StatusOK)
		w.Write(response)
	}
}

func Healthz(w http.ResponseWriter, req *http.Request) {
	w.WriteHeader(http.StatusNoContent)
	w.Write([]byte("ok"))
}

func auth(f http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		jwtMiddleware := jwtmiddleware.New(jwtmiddleware.Options{
			ValidationKeyGetter: func(token *jwt.Token) (interface{}, error) {
				return []byte(jwtSecret), nil
			},
			SigningMethod: jwt.SigningMethodHS256,
		})

		jwtMiddleware.HandlerWithNext(w, r, f)
	}
}

func main() {
	if jwtSecret == "" {
		log.Fatal("APP_JWT_SECRET environment variable not set")
	}

	router := mux.NewRouter()
	router.HandleFunc("/healthz", Healthz).Methods("GET")
	router.HandleFunc("/v1/user", auth(GetUser)).Methods("GET")

	log.Println("starting http server on port 3000")
	http.ListenAndServe("0.0.0.0:3000", router)
}
