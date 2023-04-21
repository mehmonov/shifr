<template>
<div id="app" class="min-h-screen flex items-center justify-center">
  <div class="flex flex-col items-center">
    <div class="flex flex-col mb-2">
      <label for="key" class="mb-1">Enter key:</label>
      <input v-model="key" id="key" class="rounded-md shadow-xl p-2 hover:bg-gray-100">
    </div>
    <div class="flex flex-col mb-2">
      <label for="text" class="mb-1">Enter text:</label>
      <textarea v-model="text" id="text" class="p-2 h-24 hover:bg-gray-100"></textarea>
    </div>
    <div class="flex mb-2">
      <button @click="encryptText" class="mr-2 bg-blue-500 text-white py-1 px-4 rounded hover:bg-blue-700">Encrypt</button>
      <button @click="decryptText" class="bg-green-500 text-white py-1 px-4 rounded hover:bg-green-700">Decrypt</button>
    </div>
    <p @click="copyToClipboard(encryptedText)" class="my-2">Encrypted text: {{ encryptedText }}</p>
    <p @click="copyToClipboard(decryptedText)" class="my-2">Decrypted text: {{ decryptedText }}</p>
  </div>
</div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      key: '',
      text: '',
      encryptedText: '',
      decryptedText: ''
    }
  },
  methods: {
    encryptText() {
      axios.get(`http://localhost:5000/encrypt?key=${this.key}&text=${this.text}`)
        .then(response => {
          this.encryptedText = response.data;
        });
    },
    decryptText() {
      axios.get(`http://localhost:5000/decrypt?key=${this.key}&encrypted_text=${this.encryptedText}`)
        .then(response => {
          this.decryptedText = response.data;
        });
    },
    copyToClipboard(text) {
      const message = `Bu sizning kalit so'zingiz *${this.key}*. Bu esa shifrlangan matn *${text}* . Siz kalit va matn orqali ushbu habarni o'qishingiz mumkin`;
      navigator.clipboard.writeText(message);
      alert('Nusxalandi');
      window.open('https://t.me/share/url?url=' + encodeURIComponent(message));
    }
  }
}
</script>

<style>
/* Add your styles here */
</style>
