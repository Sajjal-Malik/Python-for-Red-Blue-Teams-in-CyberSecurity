# File name: windows_message_box.py

import ctypes

def show_message_box(message, title="Python Message Box", style=0):
    """
    Displays a Windows message box with custom message, title, and style.
    
    Args:
        message (str): The message text to display in the message box.
        title (str): The title text to display in the message box title bar.
        style (int): Combination of message box style flags (e.g., MB_OK, MB_ICONINFORMATION).
                    Refer to Microsoft documentation for all available style options.
    
    Returns:
        int: The ID of the button clicked by the user (e.g., IDOK, IDCANCEL, IDYES, IDNO).
    """
    # Load the user32.dll library which contains the MessageBoxW function
    user32 = ctypes.windll.user32

    # Call the MessageBoxW function (W indicates Unicode/wide-character version)
    # Parameters:
    # 1. hWnd (HWND): Handle to the owner window (None means no owner window)
    # 2. lpText (LPCWSTR): Pointer to the message text to display (Unicode string)
    # 3. lpCaption (LPCWSTR): Pointer to the title text for the message box (Unicode string)
    # 4. uType (UINT): Combination of flags specifying contents and behavior of the message box
    return user32.MessageBoxW(None, message, title, style)

if __name__ == "__main__":
    # Example 1: Display a simple "OK" message box
    show_message_box("This is a test message from Python!", "Test Application with Python")

    # Example 2: Display an information message box with "OK" button and information icon
    # Define message box style constants
    MB_OK = 0x00000000          # OK button only
    MB_ICONINFORMATION = 0x00000040  # Information icon
    # Show message box with combined styles using bitwise OR
    show_message_box("Information about something.", "Information", MB_OK | MB_ICONINFORMATION)

    # Example 3: Display a message box with Yes/No buttons and a question icon
    MB_YESNO = 0x00000004       # Yes and No buttons
    MB_ICONQUESTION = 0x00000020  # Question mark icon
    # Define possible return values
    IDYES = 6  # Return value when user clicks 'Yes'
    IDNO = 7   # Return value when user clicks 'No'
    
    # Show message box and capture the user's response
    result = show_message_box("Do you want to continue?", "Question", MB_YESNO | MB_ICONQUESTION)

    # Process the user's response
    if result == IDYES:
        print("User clicked Yes.")
    elif result == IDNO:
        print("User clicked No.")