import streamlit as st

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
