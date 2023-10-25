import streamlit as st
import json

# Define the options for each configuration
options = {
    'Theme': ['Light', 'Dark'],
    'Password Protection': ['Yes', 'No'],
    'Draw Animation': ['Yes', 'No']
    # Add more configuration options here
}

# Function to save the config file
def save_config(config_name, config_options):
    with open(f'{config_name}.config', 'w') as f:
        json.dump(config_options, f)
    st.success(f'Config file {config_name}.config saved successfully!')

# Function to load the config file
def load_config(config_name):
    try:
        with open(f'{config_name}.config', 'r') as f:
            config_options = json.load(f)
        st.success(f'Config file {config_name}.config loaded successfully!')
        return config_options
    except FileNotFoundError:
        st.error(f'Config file {config_name}.config not found!')
        return None

# Main Streamlit app
def main():
    st.title('Config File Management')

    # Get the user login
    user_login = st.text_input('User Login')

    # Create a unique config name based on user login
    config_name = user_login

    # Create a dictionary to store the selected options
    config_options = {}

    # Iterate over each configuration option
    for option, choices in options.items():
        # Create a radio button widget for each option
        selected_option = st.radio(option, choices)
        # Store the selected option in the config_options dictionary
        config_options[option] = selected_option

    # Save button
    if st.button('Save Config'):
        save_config(config_name, config_options)

    # Load button
    if st.button('Load Config'):
        loaded_options = load_config(config_name)
        if loaded_options:
            for option, selected_option in loaded_options.items():
                st.write(f'{option}: {selected_option}')

# Run the app
if __name__ == '__main__':
    main()
