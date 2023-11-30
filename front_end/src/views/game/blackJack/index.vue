<template>
  <div>
    <el-button type="primary" @click="onlinePlay">匹配对手</el-button>
  </div>
</template>
<script>
export default {
  methods: {
    onlinePlay() {
      const gameClient = new EventSource(process.env.BASE_URL + '/game/online?game=black_jack', { withCredentials: true });
      var self = this;
      gameClient.addEventListener('message', event => {
        console.log(event.data);
      }, false);
      gameClient.onerror = function(e) {
        if (EventSource.CLOSED == e.target.readyState) {
          console.log('game client close');
          gameClient.close();
        }
      };
    }
  }
}
</script>