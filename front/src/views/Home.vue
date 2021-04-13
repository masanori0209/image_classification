<template>
  <div class="home">
    <!-- ヘッダー部 -->
    <Header/>
    <!-- アップロードフォーム -->
    <Form
      :parameter=parameter
      :loadingStatus=loadingStatus
      :createAIAnalyticsLog=createAIAnalyticsLog
      :deleteFile=deleteFile
    />
    <!-- AI analysisのログテーブル -->
    <LogTable
      :aiAnalysisLog=aiAnalysisLog
      :loadingStatus=loadingStatus
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Header from '@/components/Header.vue'
import Form from '@/components/Form.vue'
import LogTable from '@/components/LogTable.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Form,
    LogTable
  },
  computed: {
    // Vuexからステート, アクションの呼び出し
    ...mapState('aiAnalysisLog', ['aiAnalysisLog', 'loadingStatus']),
  },
  data () {
    return {
      parameter: {
        imageFile: null, // 画像データ
        readType: 'v1', // AI側の呼び出しタイプ（'v1': AI）
      }
    }
  },
  methods: {
    // 画像データを送る
    createAIAnalyticsLog () {
      let createFile = new FormData()
      createFile.append('name', this.parameter.imageFile.name)
      createFile.append('read_type', this.parameter.readType)
      createFile.append('image', this.parameter.imageFile)
      this.$store.dispatch('aiAnalysisLog/createAIanalysisLog', createFile)
      this.parameter = {
        imageFile: null,
        readType: 'v1'
      }
    },
    // 送信前の画像削除
    deleteFile () {
      this.$buefy.dialog.confirm({
          message: '送信前のデータを削除しますがよろしいでしょうか？',
          onConfirm: () => { this.parameter.imageFile = null }
      })
    },
  },
  mounted () {
    this.$store.dispatch('aiAnalysisLog/getAIanalysisLog')
  },
}
</script>
