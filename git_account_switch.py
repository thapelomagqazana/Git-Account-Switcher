import subprocess

# Define your Git configurations for different accounts
git_configs = {
    'gitlab': {
        'user.name': 'thmagqa022',
        'user.email': 'thmagqa022@student.wethinkcode.co.za'
    },
    'github': {
        'user.name': 'thapelomagqazana',
        'user.email': 'tapsmcgzee8@gmail.com'
    }
}

def commit_message():
    commit_message = input("Enter your commit message: ")
    subprocess.run(['git', 'commit', '-m', commit_message])


def set_git_config(config):
    """Set Git configurations for the selected account."""
    for key, value in config.items():
        subprocess.run(['git', 'config', '--global', key, value])

def display_details(account):
    print("Email:", account["user.email"])
    print("Name:", account["user.name"])

def main():
    print("""Welcome to Git Account Switcher. This script was designed by Thapelo Magqazana\n""")
    print("Select Git account:")
    print("type 'w' for Gitlab")
    print("type 'p' for GitHub")
    print()
    choice = input("Enter your choice (w/p): ")
    print()

    if choice == "w":
        set_git_config(git_configs["gitlab"])
        print("Switched to GitLab account.")
        display_details(git_configs['gitlab'])
        commit_message()
    elif choice == "p":
        set_git_config(git_configs['github'])
        print("Switched to GitHub account.")
        display_details(git_configs['github'])
        commit_message()
    else:
        print("Invalid choice. Please enter 'w' or 'p'")

if __name__ == "__main__":
    main()