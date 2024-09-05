import worker as w


class main:
    
    path = "/qt/iaf"
    
    repo = "iaf-dc-backend"
    
    branch = "develop"
    
    queues = [
        "iaf-os-dev",
        "iaf-upload-dev",
        "iaf-import-dev",
        "iaf-validation-field-mapping-dev",
        "iaf-validation-field-dev",
        "iaf-validation-data-mapping-dev",
        "iaf-validation-data-dev",
        "iaf-mdb-publishing-dev"
    ]
    
    memory = 1024
    
    terminal = "iTerm"
    
    process_workers = w.worker(queues, memory, path, repo, branch, terminal)
    
    process_workers.run()
    
if __name__ == "__main__":
    main()