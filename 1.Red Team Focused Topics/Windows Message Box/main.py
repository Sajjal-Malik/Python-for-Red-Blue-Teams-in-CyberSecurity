# File name: windows_message_box.py

import ctypes

def show_message_box(message_text, window_title="Python Message Box", dialog_style=0):
    """
    Displays a Windows message box with custom message, title, and style.
    
    Args:
        message_text (str): The text to display in the message box.
        window_title (str): The text to display in the message box title bar.
        dialog_style (int): Combination of message box style flags (e.g., OK_BUTTON, INFORMATION_ICON).
    
    Returns:
        int: The ID of the button clicked by the user (e.g., OK_BUTTON_ID, CANCEL_BUTTON_ID).
    """
    # Load the user32.dll library which contains the MessageBoxW function
    user32_library = ctypes.windll.user32

    # Call the MessageBoxW function (Unicode/wide-character version)
    # Parameters:
    # 1. owner_window_handle: Handle to the owner window (None means no owner window)
    # 2. message_text: The text to display in the message box
    # 3. window_title: The title text for the message box
    # 4. dialog_style: Flags specifying contents and behavior of the message box
    return user32_library.MessageBoxW(None, message_text, window_title, dialog_style)

if __name__ == "__main__":
    # Example 1: Display a simple "OK" message box
    show_message_box("This is a test message from Python!", "Test Application with Python")

    # Example 2: Display an information message box with "OK" button and information icon
    # Define message box style constants
    OK_BUTTON = 0x00000000          # OK button only
    INFORMATION_ICON = 0x00000040   # Information icon
    # Show message box with combined styles using bitwise OR
    show_message_box("Information about something.", "Information", OK_BUTTON | INFORMATION_ICON)

    # Example 3: Display a message box with Yes/No buttons and a question icon
    YES_NO_BUTTONS = 0x00000004     # Yes and No buttons
    QUESTION_ICON = 0x00000020      # Question mark icon
    # Define possible return values
    YES_BUTTON_ID = 6  # Return value when user clicks 'Yes'
    NO_BUTTON_ID = 7   # Return value when user clicks 'No'
    
    # Show message box and capture the user's response
    user_response = show_message_box(
        "Do you want to continue?", 
        "Question", 
        YES_NO_BUTTONS | QUESTION_ICON
    )

    # Process the user's response
    if user_response == YES_BUTTON_ID:
        print("User clicked Yes.")
    elif user_response == NO_BUTTON_ID:
        print("User clicked No.")