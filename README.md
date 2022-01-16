<p align="center">
  <img src="https://i.imgur.com/y6oijr9.png" alt="Legacy Edition" height="175" />
</p>
<p align="center">
  <strong>I'm Okay 👌</strong></br>
  <em>Team: Legacy Edition, NWHacks 2022</em></br>
  <a href="https://www.imokay.tech/" target="_blaank">Demo</a>
</p>
<p align="center">
<img alt="Vue" src="https://badges.aleen42.com/src/vue.svg" />
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi" />
<img alt="Vue" src="https://badges.aleen42.com/src/docker.svg" />
<img alt="npm" src="https://img.shields.io/npm/v/npm" />
</p>

---
This past year we've seen everything from forest fires to floods ravage families from across the globe. To combat this, we've created I'm Okay: a visual application for getting people the help they need. Leveraging real-time tools like Firebase and Twilio, Im Okay is able to quickly communicate with people in need and display to users exactly where they are and what they require.

## Tech Stack and Deployment
I'm Okay's backend is coded using fastapi and python 3.8. The frontend is coded using vue.js and the primevue framework. We use the twilio API to send real time text messaging to users and store disaster and response data within a Firebase realtime database. The data is then visualized using HarpGL. Finally we deploy with the use of AWS and Vercel.

## Demo video
<div align="center">
  <a href="https://www.youtube.com/watch?v=jSSjVQDOA_k"><img src="https://img.youtube.com/vi/jSSjVQDOA_k/0.jpg" alt="Demo"/></a>
</div>

## Live Deployment
www.imokay.tech


## Dev Setup
- Clone the repository
- Install Docker
- Run:
```bash
docker-compose up --build
```
- Navigate to localhost:3000 in your web browser
