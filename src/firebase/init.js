import firebase from 'firebase'
import firestore from 'firebase/firestore'


// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyA4wM5X9UyDaItT2EfsjKzS81ecQwXKjI4",
    authDomain: "smoothies-87321.firebaseapp.com",
    databaseURL: "https://smoothies-87321.firebaseio.com",
    projectId: "smoothies-87321",
    storageBucket: "smoothies-87321.appspot.com",
    messagingSenderId: "799126888166",
    appId: "1:799126888166:web:f1b42ee61472fcaba82527"
  };
  // Initialize Firebase
  const firebaseApp = firebase.initializeApp(firebaseConfig);

 export default firebaseApp.firestore()