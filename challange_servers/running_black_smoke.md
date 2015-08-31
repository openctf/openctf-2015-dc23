Running the blackSmoke / Banishing the Holy Angel challenges
===

1. both servers need to be run in a directory with all the *\_container files, and the given libc.so.6-d99432843a9b4f19b572345d4dd023ab
1. run `blackSmoke_server9a3ea6639b1288b8f77c51c10ca61fec highLow`. This starts a server that binds to port 11112.
1. run `holyAngel_serverc1611ac3ea9ef6f542882b526a1dcdfd`. This starts a server that binds to port 11113.
1. obtain blackSmoke_client2f94108a576e927733a74ac309a206f0. This is the challenge binary given to contestants.
1. the client contains hard-coded IP addresses for both servers - it expects to find blackSmoke\_server at 10.0.66.76:11112, and holyAngel\_server at 10.0.66.77:11113. To run this challenge, you can either patch the client with the new addresses of the servers, or set up routing such that the servers are available at those addresses.
1. additionally, at certain points in the challenge, the client will download and execute holyAngel\_container. holyAngel\_container has the same hard-coded IP address for holyAngel\_server - you'll need to apply the same fix as for the client.
1. run the blackSmoke\_client.
