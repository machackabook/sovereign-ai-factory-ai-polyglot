# Virtual NAS

Cloud persistence so the system does not depend on any single phone, Chromebook, or desktop remaining online.

- Drive / object storage used as durable blob store
- Git stores **configuration references**, never secrets
- Enclave sparsebundle remains encrypted offline; gateway never serves its contents to external agents
