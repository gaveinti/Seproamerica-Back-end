/*import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging/sw";

importScripts("https://www.gstatic.com/firebasejs/7.4/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/7.4/firebase-messaging-compat.js");


const firebaseApp = initializeApp({
    apiKey: "AIzaSyAgxBo5asf0B7RPrMW8o1t7qF-lAwPxt1M",
    authDomain: "seproamerica-81c1f.firebaseapp.com",
    projectId: "seproamerica-81c1f",
    storageBucket: "seproamerica-81c1f.appspot.com",
    messagingSenderId: "1052573241503",
    appId: "1:1052573241503:web:2c662c0ee8b2eb407bd2aa",
    measurementId: "G-R8PVY8CQHR"
});
const messaging = getMessaging(firebaseApp);*/

// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/7.4/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.4/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.


firebase.initializeApp({
    apiKey: "AIzaSyAgxBo5asf0B7RPrMW8o1t7qF-lAwPxt1M",
    authDomain: "seproamerica-81c1f.firebaseapp.com",
    projectId: "seproamerica-81c1f",
    storageBucket: "seproamerica-81c1f.appspot.com",
    messagingSenderId: "1052573241503",
    appId: "1:1052573241503:web:2c662c0ee8b2eb407bd2aa",
    measurementId: "G-R8PVY8CQHR"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
