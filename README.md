Scrum Poker
===========

Scrum Poker is a real-time WebSocket-based planning poker application built with Django, Django Channels, and WebSockets. It allows teams to collaboratively estimate story points for agile development.

Features
--------

-   **Real-time voting**: Users can submit their votes and see participation updates instantly.
-   **Vote masking**: Votes remain hidden until revealed.
-   **WebSocket communication**: Ensures a seamless, low-latency experience.
-   **Lightweight & fast**: No unnecessary dependencies.

Installation
------------

### Prerequisites

-   Python 3.8+
-   Django
-   Django Channels
-   Redis (for WebSocket channel layer, optional but recommended)

### Setup

1.  Clone the repository:

    ```
    git clone https://github.com/nnachit/scrum-poker.git
    cd scrum-poker

    ```

2.  Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    ```

3.  Install dependencies:

    ```
    pip install -r requirements.txt

    ```

4.  Apply database migrations:

    ```
    python manage.py migrate

    ```

5.  Run the development server:

    ```
    python manage.py runserver

    ```

6.  Start the WebSocket consumer (if necessary, for async tasks):

    ```
    daphne -b 0.0.0.0 -p 8001 scrum_poker.asgi:application

    ```

Usage
-----

-   Users join a specific game room via WebSocket (`/ws/poker/<room_name>/`).
-   They submit their votes using JSON messages:

    ```
    {"action": "vote", "username": "Alice", "vote": "5"}

    ```

-   Once all votes are submitted, they can be revealed:

    ```
    {"action": "reveal"}

    ```

Future Improvements
-------------------

-   **User authentication**: Restrict votes to registered users.
-   **Persistent storage**: Store session results in a database.
-   **Custom vote options**: Allow Fibonacci, T-shirt sizing, and custom scales.
-   **Real-time discussion**: Chat integration before vote reveal.

Contributing
------------

Feel free to open issues or submit pull requests! 🎉

License
-------

MIT License. See `LICENSE` file for details.
