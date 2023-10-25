import streamlit as st

# Function to convert options to binary format
def options_to_binary(config_options):
    binary_string = ''
    for option, choices in options.items():
        selected_option = config_options[option]
        binary_string += '1' if selected_option == choices[0] else '0'
    return int(binary_string, 2)

# Function to convert binary format to options
def binary_to_options(binary_value):
    binary_string = bin(binary_value)[2:].zfill(8)
    config_options = {}
    for i, (option, choices) in enumerate(options.items()):
        selected_option = choices[0] if binary_string[i] == '1' else choices[1]
        config_options[option] = selected_option
    return config_options

# Function to save the config file
def save_config(config_name, config_options):
    binary_value = options_to_binary(config_options)
    with open(f'{config_name}.config', 'w') as f:
        f.write(str(binary_value))
    st.success(f'Config file {config_name}.config saved successfully!')

# Function to load the config file
def load_config(config_name):
    try:
        with open(f'{config_name}.config', 'r') as f:
            binary_value = int(f.read())
        config_options = binary_to_options(binary_value)
        st.success(f'Config file {config_name}.config loaded successfully!')
        return config_options
    except FileNotFoundError:
        st.error(f'Config file {config_name}.config not found!')
        return None

# Define the options for each configuration
options = {
    'Theme': ['Light', 'Dark'],
    'Password Protection': ['Yes', 'No'],
    'Draw Animation': ['Yes', 'No']
    # Add more configuration options here
}

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

    # Change theme dynamically based on the selected option
    if 'Theme' in config_options:
        if config_options['Theme'] == 'Dark':
            st.set_theme('dark')
        else:
            st.set_theme('light')

# Run the app
if __name__ == '__main__':
    main()
