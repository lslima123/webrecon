class ScanEngine:
    def __init__(self, target):
        self.target = target
        self.modules = []
        self.results = {}

    def register(self, name, module_func, config=None):
        """
        Registers a module with optional configuration.
        """
        self.modules.append({
            "name": name,
            "func": module_func,
            "config": config or {}
        })

    def run(self):
        for mod in self.modules:
            name = mod["name"]
            func = mod["func"]
            config = mod["config"]

            try:
                
                try:
                    data = func(self.target, config)
                except TypeError:
                    data = func(self.target)

                self.results[name] = {
                    "module": name,
                    "data": data
                }

            except Exception as e:
                self.results[name] = {
                    "module": name,
                    "error": str(e)
                }

        return {
            "target": self.target,
            "results": self.results
        }
