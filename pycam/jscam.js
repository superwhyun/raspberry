const { spawn } = require('child_process')
const express = require('express')
const net = require('net')

const cmd = 'gst-launch-1.0'
const args = ['autovideosrc','horizontal-speed=1','is-live=true',
'!', 'videoconvert',
'!', 'video/x-raw, framerate=30/1, width=320, height=240',
'!', 'vp8enc','cpu-used=5','deadline=1','keyframe-max-dist=10',
'!', 'queue','leaky=1',
'!', 'm.','webmmux','name=m','streamable=true',
'!', 'tcpserversink','host=127.0.0.1','port=5000','sync-method=2']

console.log(args)
spawn(cmd, args, { stdio: 'inherit' })

const router = express.Router()

router.get('/', (req, res) => {
   res.send(`
     <html>
       <body>
          <video width="320" height="240" controls autoplay>
             <source src="/movie" type="video/webm">
              VIDEO
          </video>
       </body>
     </html>`)
})

router.get('/movie', (req, res) => {
   const date=new Date()

   res.writeHead(200, {
       'Date': date.toUTCString(),
       'Connection': 'close',
       'Cache-Control': 'private',
       'Content-Type': 'video/webm'
   })

   const socket = net.connect(5000, () => { 
       socket.pipe(res)
   })
})

const app=express()
app.use(router)
app.listen(8080, () => console.log('Server start on 8080'))


