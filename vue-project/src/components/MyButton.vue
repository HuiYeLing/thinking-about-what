<template>
  <div>
    <!-- 默认按钮 -->
    <h1>{{ msg }}</h1>
    <el-button type="primary" >主要</el-button>
    <el-button type="success">成功</el-button>
    <el-button type="info">信息</el-button>
    <el-button type="warning">警告</el-button>
    <el-button type="danger">危险</el-button>
  </div>
</template>

<script>
import { ElButton } from 'element-plus'

export default {
  name: 'MyButton',
  components: {
    ElButton
  },
  props:{
    msg: String
  }
}
</script>