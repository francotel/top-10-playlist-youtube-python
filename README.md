# YouTube Playlist Top 10 Viewer 🎬

This project utilizes Python 🐍 to list the top 10 most viewed videos from a YouTube playlist and displays them in the console. Additionally, it uses Podman 🐳 to containerize the application and is configured with GitHub Actions 🤖 to automate various tasks.

## Requirements 📋

- Python 3.x
- Podman

## Development 🛠️

1. **Clone the repository:**
    ```bash
    git clone https://github.com/francotel/top-10-playlist-youtube-python
    cd top-10-playlist-youtube-python
    ```

2. **Set up environment variables:**
    ```bash
    export YT_API_KEY="YT_API_KEY"
    export PLAYLIST_ID="PLAYLIST_ID"
    ```

3. **Develop the project:**
    - Modify `top-10-playlist.py` to add new functionalities or improvements.

4. **Build the container image:**
    ```bash
    podman build -t youtube-top-10-playlist-viewer .
    ```

5. **Run the application in the container:**
    ```bash
    podman run --rm -e YT_API_KEY="$YT_API_KEY" -e PLAYLIST_ID="$PLAYLIST_ID" youtube-top-10-playlist-viewer
    ```

## Advantages of Using Podman Over Docker 🐳

- **No central daemon (rootless)**: Podman doesn’t require a central daemon like Docker, allowing containers to be run by non-root users. 👤

- **Same CLI as Docker**: Podman offers a Docker-like CLI, making it easy for those familiar with Docker to transition and use. 💻

- **Support for Kubernetes**: Podman has closer integration with Kubernetes, making container creation and management easier. 🚀

- **Enhanced isolation and security**: Podman provides increased security by offering more process-level isolated containers, reducing the risk of malicious attacks. 🔒

- **Portability of images and containers**: Podman's images and containers are highly portable and can be run on different operating systems without modifications. 🌐

- **OCI Standards Compliance**: Podman adheres to Open Container Initiative (OCI) standards, ensuring compatibility with other tools and platforms following these standards. 🌟

- **Multi-architecture development**: Podman is capable of running containers on different architectures, allowing multi-architecture development. 🖥️

- **Greater storage flexibility**: Podman provides more flexible storage options, allowing users to manage volumes and storage in a more detailed and versatile manner. 📦


## GitHub Actions 🚀

This repository utilizes GitHub Actions to automate the workflow. Actions are set up to run tests, build, and publish the container image when a push or pull request is made to the main branch. The repository uses secrets to securely store sensitive information like API keys.

## Contributions 🤝

Contributions are welcome! If you'd like to enhance this project, feel free to submit a pull request.

## License 📄

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.