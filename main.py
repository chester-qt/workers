import worker as w


class main:
    
    # Enter path to directory of your qualitytrade projects
    path = "/qt/iaf"
    
    # Repository name
    repo = "iaf-dc-backend"
    
    # Branch name
    branch = "develop"
    
    # Add or remove queues here
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
    
    # Memory in MB
    memory = 1024
    
    # Name of terminal (defaults to iTerm)
    terminal = "iTerm"
    
    process_workers = w.worker(queues, memory, path, repo, branch, terminal)
    
    process_workers.run()
    
if __name__ == "__main__":
    main()