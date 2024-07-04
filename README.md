# LavenderIRC

LavenderIRC is a simple IRC client implemented in Python with a GUI built using Tkinter. It allows users to connect to IRC servers, join channels, and send/receive messages in real-time.

## Features

- **Connect to IRC Servers:** Enter server details such as Server, Port, Nickname, and Channel to establish a connection.
  
- **Real-time Messaging:** Send and receive messages from IRC channels directly within the application.
  
- **Simple and Intuitive GUI:** Built using Tkinter with a Catppuccin-inspired theme for a sleek and minimalistic user interface.

## Installation

### Prerequisites

- python3 installed on your system.
- python-pip installed on your system.

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pseudify/LavenderIRC.git
   cd lavenderirc
   ```

2. **Set Up Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r dependencies.txt
   ```

4. **Run the Application:**

   ```bash
   ./lavenderirc
   ```

## Usage

- Upon running the application, enter the required server details and click "Connect" to establish a connection.
  
- Use the input box at the bottom to send messages to the IRC channel.
  
- Click "Disconnect" to disconnect from the server and return to the connection setup.

## Contribution

Contributions are welcome! If you have any suggestions, bug reports, or future requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.