<template>
  <div>
    <commonHeader/>
    <div style="width: 100%; height: auto; position: absolute; top: 70px; ">
      <div style="width: 30%; position: absolute; left: 10px; top: 10px;">
        <el-input
          style="height: 60%;"
          type="textarea"
          readonly
          resize="none"
          v-model="chatContent">
        </el-input>
        <el-input placeholder="请输入想说的话" v-model="messageInfo.message">
          <template slot="append"><el-button type="primary" @click="sendMessage">发送</el-button></template>
        </el-input>
      </div>
    </div>
    <commonFooter/>
  </div>
</template>

<script>
import commonHeader from '@/components/header.vue'
import commonFooter from '@/components/footer.vue'
export default {
  name: 'Home',
  components: {
    commonHeader,
    commonFooter
  },
  data () {
    return {
      chatContent: 'a',
      messageInfo: {
        "message": ''
      },
    }
  },
  mounted() {
    const chatEsClient = new EventSource(process.env.BASE_URL + '/chat/online', { withCredentials: true });
    var self = this;
    chatEsClient.addEventListener('chat', this.chatListener, false);
    chatEsClient.onerror = function(e) {
      if (EventSource.CLOSED == e.target.readyState) {
        console.log('client close-----');
        chatEsClient.close();
      }
    };
  },
  methods: {
    chatListener(event) {
      this.chatContent = this.chatContent.concat(event.data, '\n');
      console.log('???' + this.chatContent);
    },
    sendMessage() {
      this.$axios.post('/chat/push', this.messageInfo).then(resp =>{
        console.log('push success');
      })
    },
    logout() {
      this.$axios.get('/auth/logout').then(resp => {
        console.log(resp);
      })
    },
    test() {
      this.$axios.get('/auth/test').then(resp => {
        console.log('test fail')
      })
    }
  }
}
</script>
