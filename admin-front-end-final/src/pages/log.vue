<template>
  <div>
    <div class="btn-wrapper">
      <div class="page-title">系统日志</div>
    </div>
    <div class="main-board">
      <div class="log-panel">
        {{ log }}
      </div>
    </div>
  </div>
</template>
  
<script>
/* eslint-disable no-unused-vars */
import { ref } from 'vue'
import api from './_api';
import http from './http';
// const radio1 = ref('New York')

// import header from '../components/header'
export default {
  data(){
    return {
      log: 'Empty'
    }
  },
  components: {
    // header,
  },
  created(){
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      http.get(api.getLog, {})
        .then((res) => {
          if (res.status === 10000) {
            this.log = res.data
          } else {
            this.$message({
              type: 'error',
              message: res.msg
            });
          }
      })
    }
  },
}

</script>
<style>
.main-board {
  width: 100%;
  /* background-color: white; */
  margin-top: 24px;
}
.log-panel {
  background-color: rgb(33, 33, 33);
  max-width: calc(100% - 200px);
  height: 75vh;
  margin-left: 48px;
  overflow: scroll;
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.8);
  padding: 24px 32px;
  display: flex;
  flex-direction: column-reverse;
  font-family: monospace;
  line-height: 20px;

}
</style>