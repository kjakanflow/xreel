import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def create_directory_structure(base_path, tree_structure):
    for folder, subfolders, files in tree_structure:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f'Created directory: {folder_path}')
        for file_name, file_contents in files:
            file_path = os.path.join(folder_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(file_contents)
                logging.info(f'Created file: {file_path}')
            else:
                logging.warning(f'File already exists: {file_path}')

def main():
    base_directory = os.path.join(os.path.dirname(__file__), 'src')  # Set the base directory path to 'src' relative to the script location
    tree_structure = [
        ('components', [
            ('MainPage', [('MainPage.js', ''), ('MainPage.css', '')]),
            ('LoginPage', [('LoginPage.js', ''), ('LoginPage.css', '')]),
            ('CommentPage', [('CommentPage.js', ''), ('CommentPage.css', '')]),
            ('VideoPlayer', [('VideoPlayer.js', ''), ('VideoPlayer.css', '')]),
            ('LikingSystem', [('LikingSystem.js', ''), ('LikingSystem.css', '')]),
            ('UploadVideoPage', [('UploadVideoPage.js', ''), ('UploadVideoPage.css', '')])
        ]),
        ('assets', [
            ('images', [('logo.png', ''), ('user.png', '')])
        ]),
        ('utils', [
            ('api.js', ''),
            ('auth.js', '')
        ]),
        ('contexts', [
            ('AuthContext.js', '')
        ]),
        ('routes', [
            ('PrivateRoute.js', '')
        ]),
        ('reducers', [
            ('rootReducer.js', ''),
            ('authReducer.js', '')
        ]),
        ('actions', [
            ('authActions.js', '')
        ]),
        ('store', [
            ('store.js', '')
        ])
    ]

    create_directory_structure(base_directory, tree_structure)
    print("Tree structure created successfully.")

if __name__ == "__main__":
    main()
