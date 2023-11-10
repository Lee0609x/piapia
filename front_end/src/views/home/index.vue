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
    let source = new EventSource(process.env.BASE_URL + '/sse/test', { withCredentials: true });
    source.addEventListener('greeting', function(event) {
        console.log(event);
    }, false);
    let source2 = new EventSource(process.env.BASE_URL + '/sse/test', { withCredentials: true });
    source2.addEventListener('greeting', function(event) {
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
