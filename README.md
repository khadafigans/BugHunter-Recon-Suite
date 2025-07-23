<body>

  <h1>🕷️ BUG HUNTER — Automated Recon Toolkit</h1>
  <p>By <strong>Bob Marley</strong> | <a href="https://t.me/marleyybob123">@marleyybob123</a></p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Subdomain Enumeration via <code>Subfinder</code></li>
    <li>Live Host Discovery via <code>httpx</code></li>
    <li>Parameter Crawling via <code>Paramspider</code></li>
    <li>Endpoint Fuzzing via <code>FFUF</code></li>
    <li>XSS Scanning via <code>Dalfox</code></li>
    <li>SQLi Filtering via <code>SQLMap</code> (no scan)</li>
    <li>Colorful CLI and recon completion summary</li>
  </ul>

  <h2>📁 Directory & Output Format</h2>
  <p>All outputs are saved using the format:</p>
  <pre><code>&lt;Tool&gt;/&lt;Tool&gt;__target.com_YYMMDD.txt</code></pre>

  <ul>
    <li>Subfinder → <code>Subfinder/subfinder_target.com_250724.txt</code></li>
    <li>Httpx     → <code>Httpx/httpx__target.com_250724.txt</code></li>
    <li>Paramspider → <code>results/target.com.txt</code> (default behavior)</li>
    <li>FFUF      → <code>FFUF/FFUF__target.com_250724.txt</code></li>
    <li>Dalfox    → <code>Dalfox/Dalfox_target.com_250724.txt</code></li>
    <li>Sqlmap    → <code>Sqlmap/Sqlmap_target.com_250724.txt</code></li>
  </ul>

  <h2>🛠️ Setup Instructions</h2>
  <h3>1. Install Required Tools</h3>
  <pre><code>go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo apt install ffuf sqlmap
pip install git+https://github.com/devanshbatham/paramspider.git
go install github.com/hahwul/dalfox/v2@latest</code></pre>

  <h3>2. Clone SecLists (Optional for wordlists)</h3>
  <pre><code>git clone https://github.com/danielmiessler/SecLists.git</code></pre>

  <h3>3. Environment Variables</h3>
  <p>Make sure all tools are in your system PATH.</p>
  <pre><code># Example for Windows:
set PATH=%PATH%;C:\Users\USER\go\bin

# Example for Linux:
export PATH="$PATH:$(go env GOPATH)/bin"</code></pre>

  <h3>4. Python Requirements</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>5. Folder Setup</h3>
  <ul>
    <li>Create subfolders: <code>Subfinder</code>, <code>Httpx</code>, <code>FFUF</code>, <code>Dalfox</code>, <code>Sqlmap</code>, and <code>results</code></li>
    <li>Place your <code>main.py</code> script in the root Recon folder</li>
  </ul>

  <h2>🧪 Usage</h2>
  <pre><code>cd Recon
python main.py</code></pre>

  <h3>Options:</h3>
  <pre><code>[1] Run Subfinder
[2] Run Httpx
[3] Run Paramspider
[4] Run FFUF
[5] Run Dalfox
[6] Run Sqlmap URL filter
[7] Run ALL steps</code></pre>

  <h2>📊 Completion Output</h2>
  <pre><code>🎯 RECON COMPLETE — target.com
------------------------------------------------
📂 Subdomains      → Subfinder/subfinder_target.com_250724.txt
✅ Alive hosts     → Httpx/httpx__target.com_250724.txt
🔎 Params (FUZZ)   → results/target.com.txt
🧨 FFUF results    → FFUF/FFUF__target.com_250724.txt
🧬 XSS scan        → Dalfox/Dalfox_target.com_250724.txt
🧪 SQLi targets    → Sqlmap/Sqlmap_target.com_250724.txt
------------------------------------------------</code></pre>

  <h2>📜 License</h2>
<p>
  <strong>License & Legal Disclaimer:</strong><br>
  This project is released under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a>. It is built for educational purposes, penetration testing, and security research only. 
  <br><br>
  The tools included in this suite are powerful and capable of identifying vulnerabilities across web applications. 
  By using this software, you agree to use it <strong>only on systems and applications you own or have been explicitly authorized to test</strong>. 
  <br><br>
  Unauthorized scanning, exploitation, or enumeration of systems without consent may violate computer misuse laws and could result in legal consequences.
  The creator and contributors are <strong>not responsible</strong> for any misuse or damage caused by this tool.
  <br><br>
  Stay ethical. Hack responsibly. 💀
</p>

</body>
</html>
