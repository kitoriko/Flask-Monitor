To run the Flask application locally without Docker, you'll need to follow these steps:

### Prerequisites

1. Make sure you have Python 3.x installed. You can download it from [Python's official website](https://www.python.org/downloads/).
2. Install `pip` if it's not already installed. You can check by running `pip --version` in the terminal.

### Steps

1. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python3 -m venv myenv
    ```

    - Activate the virtual environment:
        - On macOS and Linux:
            ```bash
            source myenv/bin/activate
            ```
        - On Windows:
            ```bash
            .\myenv\Scripts\activate
            ```

2. **Install Dependencies**
    - Run the following command to install the dependencies:
        ```bash
        pip install -r requirements.txt
        ```

3. **Provide Kubernetes Configuration**
    - Make sure you have a valid `kubeconfig` file. By default, the Kubernetes client will look for this file in your home directory under `.kube/config`.

4. **Run the Application**
    ```bash
    python app.py
    ```
    This will start the Flask development server, and the application should be accessible at `http://127.0.0.1:5000/`.

5. **Check Logs**
    - The application logs will be saved in a file named `app.log` in the same directory as your `app.py`.

### Note

- The application is configured to run in debug mode (`app.run(debug=True)`), which is suitable for development but not for production.
- If you're running the application on a machine that doesn't have access to the Kubernetes cluster, make sure to provide the `kubeconfig` file that has the necessary credentials.

That's it! You should now be able to run your Flask application locally and see the uptime information of your Kubernetes clusters.