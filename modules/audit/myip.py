from core.vectors import PhpCode, ShellCmd, ModuleExec, Os
from core.module import Module
from core import modules


class Myip(Module):
    """Get my ip."""

    def init(self):

        self.register_info(
            {
                'author': [
                    'Sander Ferdinand'
                ],
                'license': 'MIT'
            }
        )

        # self.register_arguments([
        #     {'name': '-real', 'help': 'Filter only real users', 'action': 'store_true', 'default': False},
        #     {'name': '-vector', 'choices': ('posix_getpwuid', 'file', 'fread', 'file_get_contents', 'base64')}
        # ])

    def run(self):
        result = PhpCode("""print $_SERVER['REMOTE_ADDR'];""").run()
        result = "$_SERVER['REMOTE_ADDR']: " + result
        return result.rstrip('\n')
