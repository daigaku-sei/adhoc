import streamlit as st
import json

# Define the options
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6', 'Option 7', 'Option 8']

# Function to save the config file
def save_config(config_name, selected_option):
    config = {'option': selected_option}
    with open(f'{config_name}.config', 'w') as f:
        json.dump(config, f)
    st.success(f'Config file {config_name}.config saved successfully!')

# Function to load the config file
def load_config(config_name):
    try:
        with open(f'{config_name}.config', 'r') as f:
            config = json.load(f)
        selected_option = config['option']
        st.success(f'Config file {config_name}.config loaded successfully!')
        return selected_option
    except FileNotFoundError:
        st.error(f'Config file {config_name}.config not found!')
        return None

# Main Streamlit app
def main():
    st.title('Config File Management')

    # Get the user login
    user_login = st.text_input('User Login')

    # Create a unique config name based on user login
    config_name = f'{user_login}.config'

    # Create a radio button widget
    selected_option = st.radio('Options', options)

    # Save button
    if st.button('Save Config'):
        save_config(config_name, selected_option)

    # Load button
    if st.button('Load Config'):
        loaded_option = load_config(config_name)
        if loaded_option:
            st.write(f'Selected option: {loaded_option}')

# Run the app
if __name__ == '__main__':
    main()
