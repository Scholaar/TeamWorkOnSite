<template>
  <div class="container">
    <el-button type="primary" @click="sentAll">一键发送</el-button>
    <div class="main">
      <el-upload
      drag
      action="http://127.0.0.1:5000/api/upload"
      accept=".excel,.xls,.xlsx"
      >
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">
          将文件拖到此处，或<em>点击上传</em>
        </div>
        <template #tip>
          <div class="el-upload__tip">只能上传.excel/.xls/.xlsx文件，且不超过500kb</div>
        </template>
      </el-upload>
    </div>
  </div>
</template>

<script setup>
import { UploadFilled } from '@element-plus/icons-vue'
import request from '../utils/requests'
const onSuccess = (res, file, fileList) => {
  // 如果成功路由跳转到task页面，否则提示错误
  if (res.mesg === 'ok') {
    console.log(res)
    console.log(file)
    console.log(fileList)
    router.push('/task')
  } else {
    console.log(res)
  }
}
const sentAll = async () => {
    const res = await request({
        url: '/api/sent',
        method: 'get'
    })
    console.log(res.data)
      ElNotification({
      title: 'Success',
      message: res.data.mesg,
      type: 'success',
    })
}
</script>

<style lang="less" scoped>
.container{
  flex: 1 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.main{
  width: 500px;
  padding: 20px;
}
</style>