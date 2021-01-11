const url_socket = process.env.ENV_RPGCHRONICLER_URL || "ws://localhost:8000"
const socket = new WebSocket(url_socket);
