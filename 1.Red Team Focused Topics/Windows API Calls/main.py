import ctypes

def show_message_box(message, title="Python Message Box", style=0):
    """
    Displays a Windows message box.

    Args:
        message (str): The message text to display.
        title (str): The title of the message box.
        style (int): A combination of message box style flags (e.g., MB_OK, MB_ICONINFORMATION).
                     See Microsoft documentation for MessageBox styles for more options.
    Returns:
        int: The ID of the button clicked by the user (e.g., IDOK, IDCANCEL).
    """
    # Load the user32.dll library which contains MessageBoxW
    user32 = ctypes.windll.user32

    # Call the MessageBoxW function (W for wide-character/Unicode strings)
    # Parameters:
    # 1. hWnd (HWND): Handle to the owner window (None for no owner).
    # 2. lpText (LPCWSTR): The message to be displayed.
    # 3. lpCaption (LPCWSTR): The title of the message box.
    # 4. uType (UINT): The contents and behavior of the message box.
    return user32.MessageBoxW(None, message, title, style)

if __name__ == "__main__":
    # Example usage:
    # Display a simple "OK" message box
    show_message_box("This is a test message from Python!", "Test Application with Python")

    # Display an information message box with "OK" button
    MB_OK = 0x00000000
    MB_ICONINFORMATION = 0x00000040
    show_message_box("Information about something.", "Information", MB_OK | MB_ICONINFORMATION)

    # Display a message box with Yes/No buttons and a question icon
    MB_YESNO = 0x00000004
    MB_ICONQUESTION = 0x00000020
    IDYES = 6  # Return value for 'Yes'
    IDNO = 7   # Return value for 'No'
    result = show_message_box("Do you want to continue?", "Question", MB_YESNO | MB_ICONQUESTION)

    if result == IDYES:
        print("User clicked Yes.")
    elif result == IDNO:
        print("User clicked No.")