<h1>SSL File Transfer GUI</h1>

This project implements a secure file transfer system in Python using SSL sockets. It features:

<ul>
  <li>Parallel control and data channels</li>
  <li>SSL encryption using self-signed certificates</li>
  <li>A simple graphical interface using Tkinter</li>
</ul>

<h2>Features</h2>
<ul>
  <li>Secure transfer using SSL</li>
  <li>Separate control and data channels</li>
  <li>GUI for both sender and receiver</li>
  <li>Cross-platform (Linux, Windows)</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Tkinter</li>
</ul>

<h2>To Generate SSL Certificates</h2>

```
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```

<h2>How to Run</h2>
<ol>
  <li>Generate SSL certificates (see above).</li>
  <li>Run <code>receiver_ssl.py</code> on the receiving machine.</li>
  <li>Run <code>sender_ssl.py</code> on the sending machine.</li>
  <li>In the sender GUI, provide the receiver’s IP address and select a file to send.</li>
</ol>

<h2>Files</h2>
<ul>
  <li><b>sender_ssl.py</b>: GUI to select file and send via SSL</li>
  <li><b>receiver_ssl.py</b>: GUI to receive and save file securely</li>
  <li><b>cert.pem / key.pem</b>: Example SSL certificates (generate your own for production use)</li>
</ul>

<h2>Notes</h2>
<ul>
  <li>This implementation is intended for educational/demo purposes only.</li>
  <li>For production, ensure certificates are securely generated and verified.</li>
</ul>

<h2>License</h2>
This project is open-source and free to use for educational purposes.
