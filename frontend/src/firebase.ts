import firebase from "firebase/compat";

const FIREBASE_CONFIG = {
    apiKey: "AIzaSyDfzIpFWkzgemD9fEWeZJED7RXlGgwCSWw",
    authDomain: "disaster-recovery-nw.firebaseapp.com",
    databaseURL: "https://disaster-recovery-nw-default-rtdb.firebaseio.com",
    projectId: "disaster-recovery-nw",
    storageBucket: "disaster-recovery-nw.appspot.com",
    messagingSenderId: "33135188422",
    appId: "1:33135188422:web:41f5faa3d4060369287ac7",
    measurementId: "G-XJKSTKXYB2"
}

firebase.initializeApp(FIREBASE_CONFIG)
const db = firebase.database();

export {db}
