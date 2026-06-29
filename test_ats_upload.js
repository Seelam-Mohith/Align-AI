const fs = require('fs');
const path = require('path');
const http = require('http');

async function testAtsUpload() {
  try {
    const filePath = path.join(__dirname, 'test_resume.pdf');
    
    if (!fs.existsSync(filePath)) {
      console.error('❌ Test PDF not found:', filePath);
      process.exit(1);
    }
    
    const fileContent = fs.readFileSync(filePath);
    const boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW';
    const body = `--${boundary}\r\nContent-Disposition: form-data; name="file"; filename="test_resume.pdf"\r\nContent-Type: application/pdf\r\n\r\n${fileContent.toString('binary')}\r\n--${boundary}--`;
    
    console.log('📤 Uploading test resume to http://localhost:5000/api/ats/upload...');
    
    const options = {
      hostname: 'localhost',
      port: 5000,
      path: '/api/ats/upload',
      method: 'POST',
      headers: {
        'Content-Type': `multipart/form-data; boundary=${boundary}`,
        'Content-Length': Buffer.byteLength(body),
      },
    };
    
    const req = http.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => {
        console.log(`Status: ${res.statusCode}`);
        if (res.statusCode === 200) {
          try {
            const json = JSON.parse(data);
            console.log('✅ Upload successful!');
            console.log('Response:', JSON.stringify(json, null, 2));
          } catch (e) {
            console.log('Response:', data);
          }
        } else {
          console.log('❌ Error:', data);
        }
      });
    });
    
    req.on('error', (e) => {
      console.error('❌ Request failed:', e.message);
      process.exit(1);
    });
    
    req.write(body, 'binary');
    req.end();
  } catch (error) {
    console.error('❌ Test failed:', error.message);
    process.exit(1);
  }
}

testAtsUpload();
