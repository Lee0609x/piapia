<template>
  <div>
    <el-button type="primary" @click="onlinePlay">匹配对手</el-button>
    <canvas id="pixi"></canvas>
  </div>
</template>
<script>
//import * as PIXI from 'pixi.js'
export default {
  name: "ConnectionsLayer",
  mounted() {
//    this.drawPixi();
  },
  data() {
    return {
      gameClient: null,
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
    },
    // drawPixi() {
    //   var canvas = document.getElementById('pixi')

    //   const app = new PIXI.Application({
    //     width: window.innerWidth,
    //     height: window.innerHeight,
    //     antialias: true,
    //     transparent: true,
    //     view: canvas,
    //   })

    //   let graphics = new PIXI.Graphics() 
    //   graphics.lineStyle(8, 0x000000)

    //   //start
    //   graphics.moveTo(300, 250)
    //   //end
    //   graphics.lineTo(500, 250)

    //   app.stage.addChild(graphics)
    // },
  }
}
</script>