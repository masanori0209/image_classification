<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
@import 'https://cdn.jsdelivr.net/npm/@mdi/font@5.8.55/css/materialdesignicons.min.css';
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500&display=swap');

#app {
  font-family: 'Noto Sans JP', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

th, td {
  white-space: nowrap;
  text-overflow: ellipsis;
  max-width: 360px;
  overflow: hidden;
}
</style>
