<template>
  <div>
    <commonHeader/>
    <div>
      <el-row style="padding-top: 80px; padding-left: 10px; padding-right: 10px;">
        <el-col :xs="18" :sm="18" :md="18" :lg="18" :xl="18">
          <div>
            <router-view></router-view>
          </div>
        </el-col>
        <el-col :xs="6" :sm="6" :md="6" :lg="6" :xl="6">
          <div>
            <el-input
              rows="25"
              id="chatTextarea"
              type="textarea"
              readonly
              resize="none"
              v-model="chatContent"
              >
            </el-input>
            <el-input
              placeholder="请输入想说的话" 
              v-model="messageInfo.message" 
              type="textarea"
              resize="none"
              rows="3"
              >
            </el-input>
            <el-button type="primary" @click="sendMessage" style="position: relative; width: 20%; left:40%; bottom: 0px;">发送</el-button>
          </div>
        </el-col>
      </el-row>
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
      chatContent: '这是一个聊天室，你所发送的消息会被所有在线用户接收\n',
      messageInfo: {
        "message": ''
      }
    }
  },
  mounted() {
    const chatEsClient = new EventSource(process.env.BASE_URL + '/chat/online', { withCredentials: true });
    var self = this;
    chatEsClient.addEventListener('chat', this.chatListener, false);
    chatEsClient.onerror = function(e) {
      if (EventSource.CLOSED == e.target.readyState) {
        console.log('client close');
        chatEsClient.close();
      }
    };
  },
  methods: {
    chatListener(event) {
      this.chatContent = this.chatContent.concat(event.data, '\n');
      //滚动条保持最底部
      const textarea = document.getElementById('chatTextarea');
      textarea.scrollTop = textarea.scrollHeight;
      //this.notice();
    },
    sendMessage() {
      this.$axios.post('/chat/push', this.messageInfo).then(resp =>{
        console.log('push message');
        this.messageInfo.message = '';
      })
    },
    notice() {
      Notification.requestPermission().then(function(permission) {
        if (permission === 'granted') {
          // 创建通知对象
          var notification = new Notification('浏览器通知事件', {
            body: '测试',
          });
          // 处理通知点击事件
          notification.onclick = function() {
            console.log('点击通知的事件');
          };
        }
      });
    }
  }
}
</script>
