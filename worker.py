import subprocess as sb

class worker: 
    def __init__(self, queues, memory, path, repo, branch = "develop"):
        self.queues = queues
        self.memory = memory
        self.path = path
        self.repo = repo
        self.branch = branch
        
    def run(self):
        self.processWorkers()
    
    def processWorkers(self):
        path = f"cd ~{self.path}/{self.repo}"
        
        for i in range(len(self.queues)):
            
            queue = self.queues[i]
            
            branch = f"git checkout {self.branch}"
            command = f"php artisan queue:work redis --queue={queue} --memory={self.memory}"
            
            apple_script = f'''
                            tell application "iTerm"
                                activate
                                tell current window
                                    create tab with default profile
                                    tell current session of current tab to write text "{path}"
                                    tell current session of current tab to write text "{branch}"
                                    tell current session of current tab to write text "{command}"
                                end tell
                            end tell
                            '''
            
            sb.run(["osascript", "-e", apple_script])
        
            