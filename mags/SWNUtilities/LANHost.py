import os, sys, subprocess
from SWNUtilities.get_ip_addresss import get_ip_address

LOCAL_IP = get_ip_address()
PORT = '8000'
venv_script_path = '.\\..\\venv\\Scripts\\python'

start_command = f'./manage.py runserver {LOCAL_IP}:{PORT}'

# is virtualenv active?
def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix


def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix


if __name__ == '__main__':

    if not in_virtualenv():  # activate virtualenv if not active
        print('activating venv')
        os.system(f'{venv_script_path} manage.py runserver {LOCAL_IP}:{PORT}')
    else:
        os.system(f'python manage.py runserver {LOCAL_IP}:{PORT}')