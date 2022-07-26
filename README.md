# Conductor take-home DevOps exercise

Please allocate up to two hours to complete the exercises. You may present missing components, or make changes to your submission during the follow-up conversation. Please send the relevant files to <workwithus-engineering@conductortech.com> upon completion of the exercises.

We’re excited to see what you come up with!

-[Your future colleagues](https://www.conductortech.com/about-us)

## Architecture exercise

The [Go playground provides](https://play.golang.org) the ability to run code directly through the web browser. We would like you to design a high level diagram for a backend architecture to run arbitrary code samples in any programming language, and send the results back.

You can assume that there is already a frontend application capable of sending the code sample payload via WebSocket, along with the name of the programming language and its version. How would you design the architecture needed to safely execute arbitrary code in any programming language?

You may use the following diagram applications:
- AWS: [Cloudcraft](https://cloudcraft.co)
- GCP: [Cacoo](https://cacoo.com/templates/gcp-diagram-software)

## Technical exercise

Deploy a Go binary to the public cloud provider of your choice, and expose its public HTTP endpoint through a TLS-terminated load balancer.

For your convenience, the [source file](https://github.com/AtomicConductor/takehome-devops-exercise/blob/master/main.go) is included, along with pre-compiled [GNU/Linux](https://github.com/AtomicConductor/takehome-devops-exercise/blob/master/server-linux) and [OS X](https://github.com/AtomicConductor/takehome-devops-exercise/blob/master/server-darwin) binaries.

You do not need to put a reverse proxy in front of the Go HTTP server.

### Authentication

Note that the environment variable `APP_JWT_SECRET` must be provided to the binary, else the program will return an error. You may use the following JWT to test the `/v1/user` HTTP endpoint.
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE1NTQ3NTU1NTUsImV4cCI6MjU1NDc1NTUwMCwiaWF0IjoxNTU0NzU1NTAwLCJqdGkiOiI5ZmRmMGE2Ni00YzllLTRlOTktODc4MC05YjdlOTNlMjFlMjciLCJ1c2VyX2lkIjoiMTA1YjM1MTgtNjQ2ZC00NjNlLWFkZGEtZDJiOTM5YzJkMDZkIiwidXNlcl9mdWxsX25hbWUiOiJCZXJ0cmFtIEdpbGZveWxlIiwidXNlcl9lbWFpbCI6Im51bGxAcGllZHBpcGVyLmNvbSJ9.-A8Gx18iTikKpedcxDlgcc7D8GMWFix0709Vfpbo1SI
```
Note that the JWT uses the HS256 algorithm and `sekret` as the secret (`APP_JWT_SECRET`.)

### HTTP endpoints

#### GET /healthz
Privately exposed endpoint that responds with a 204 status code. This endpoint can be used for health checks.

#### GET /v1/user
Publicly exposed endpoint that returns information about the user making the request. Requires a valid JWT.
