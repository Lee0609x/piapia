<template>
  <div>
    <commonHeader/>
    <div style="width: 100%; height: auto; position: absolute; top: 70px; ">
      <el-button @click="logout">test</el-button>
      <br/>
      <el-button @click="test">test2</el-button>
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
    }
  },
  mounted() {
    let source = new EventSource(process.env.BASE_URL + '/chat/online', { withCredentials: true });
    source.addEventListener('chat', function(event) {
        console.log(event);
    }, false);
  },
  methods: {
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
