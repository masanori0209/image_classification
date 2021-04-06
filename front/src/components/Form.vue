<template>
  <section class="section">
    <!-- アップロードフォーム -->
    <b-field>
      <b-upload
        v-model="parameter.imageFile"
        drag-drop>
        <section class="section">
          <div class="content has-text-centered">
            <p>
              <b-icon
                  icon="upload"
                  size="is-large">
              </b-icon>
            </p>
            <p>ドラッグ＆ドロップもしくはこちらをクリックして下さい</p>
          </div>
        </section>
      </b-upload>
      <div class="block" v-if="!isEmptyFile">
        <span
          class="tag is-primary">
          {{parameter.imageFile.name}}
          <button class="delete is-small"
              type="button"
              @click="deleteFile()">
          </button>
        </span>
      </div>
    </b-field>
    <!-- 画像認識APIの種類を選ぶUI -->
    <!-- <div class="block">
      <b-radio v-model="parameter.readType"
        name="read-type"
        native-value="v1">
        モックアップ
      </b-radio>
      <b-radio v-model="parameter.readType"
        name="read-type"
        native-value="v2">
        AI
      </b-radio>
    </div> -->
    <!-- 送信ボタン -->
    <div class="block">
      <b-button
        type="is-primary"
        @click="createAIAnalyticsLog()"
        icon-left="head-sync-outline"
        :loading="isLoading"
        :disabled="isEmptyFile">
        {{ isLoading ? '送信中です' : '画像を送信' }}
      </b-button>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Form',
  props: {
    parameter: {
      type: Object,
      require: true
    },
    loadingStatus: {
      type: String,
      require: true
    },
    createAIAnalyticsLog: {
      type: Function,
      require: true
    },
    deleteFile: {
      type: Function,
      require: true
    },
  },
  computed: {
    isLoading () {
      return this.loadingStatus === 'create'
    },
    isEmptyFile () {
      return this.parameter.imageFile === null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
