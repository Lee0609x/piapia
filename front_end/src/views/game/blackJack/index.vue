<template>
  <div>
    <el-button type="primary" @click="onlinePlay">匹配对手</el-button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      gameClient: null
    }
  },
  methods: {
    onlinePlay() {
      if (this.gameClient == null) {
        this.gameClient = new EventSource(process.env.BASE_URL + '/game/online?game=black_jack', { withCredentials: true });
        var self = this;
        this.gameClient.addEventListener('message', event => {
          console.log(event.data);
        }, false);
        this.gameClient.onerror = function(e) {
          if (EventSource.CLOSED == e.target.readyState) {
            console.log('game client close');
            gameClient.close();
          }
        };
      } else {
        console.log('游戏通讯已经开启，无法创建新的通讯');
      }
    }
  }
}
</script>