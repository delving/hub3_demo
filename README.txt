
- vm restart issue -
Due to the demo vm mounting the project dir of the host system,
you can not restart the vm in the virtualbox GUI.

You have to start it with vagrant up, otherwise project dir will be empty and all services will fail
