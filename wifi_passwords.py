import subprocess


def extract_wifi_passwords():
    """Extracting Windows Wi-Fi passwords into .txt file"""

    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('Windows-1251').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('Windows-1251').split(
            '\n')

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
        except IndexError:
            password = None

        print(f'Profile: {profile}\nPassword: {password}\n\n')


def main():
    extract_wifi_passwords()


if __name__ == '__main__':
    main()
