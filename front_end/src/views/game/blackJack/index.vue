<template>
  <div id="gameBox" style="width: 100%; height: 100%;">
    <!-- <el-button type="primary" @click="onlinePlay">匹配对手</el-button> -->

  </div>
</template>
<script>
import * as PIXI from 'pixi.js';
export default {
  mounted() {
    const game = new PIXI.Application({
    });
    const gameBox = document.getElementById('gameBox');
    gameBox.appendChild(game.view);
    game.renderer.backgroundColor = 0xF9F9F9;
    game.renderer.autoResize = true;
    //game.renderer.resize(gameBox.style.width, gameBox.style.height);
    game.loader.add('bunny', '/static/images/test.png').load((loader, resources) => {
      const bunny = new PIXI.Sprite(resources.bunny.texture);

      // Setup the position of the bunny
      bunny.x = game.renderer.width / 2;
      bunny.y = game.renderer.height / 2;

      // Rotate around the center
      bunny.anchor.x = 0.5;
      bunny.anchor.y = 0.5;

      // Add the bunny to the scene we are building
      game.stage.addChild(bunny);

      // Listen for frame updates
      game.ticker.add(() => {
          // each frame we spin the bunny around a bit
          bunny.rotation += 0.01;
      });
    });

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
    }
  }
}
</script>
<style>

</style>