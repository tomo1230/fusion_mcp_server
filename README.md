# Fusion MCP Server addin 

**バージョン: 0.7.80 (Beta)　ファイル連携バージョン**

Autodesk Fusion (360) を外部からプログラム的に制御するためのアドインです。このスクリプトは、Fusion 内でローカルサーバーとして動作し、指定されたテキストファイルを監視します。ファイルにJSON形式のコマンドが書き込まれると、それを即座に実行し、3Dモデルの作成、編集、情報取得を自動化します。

このプロジェクトは、Kanbara Tomonori氏によって開発されました。

-   **作者:** Kanbara Tomonori
-   **X (旧Twitter):** [@tomo1230](https://x.com/tomo1230)
-   **ライセンス:** 本ソースコードはプロプライエタリかつ機密情報です。無断での複製、修正、配布、使用は固く禁じられています。

---

## 概要

このアドインは、Fusion のモデリングプロセスを自動化・効率化するための強力なツールです。外部アプリケーションやスクリプトからJSONコマンドを送信するだけで、Fusion を直接操作することなく、複雑な形状の作成や繰り返し作業を実行できます。

**主な仕組み:**
1.  **サーバー起動**: Fusion のUIから「連携開始」ボタンをクリックしてサーバーを起動します。
2.  **コマンド監視**: アドインはバックグラウンドで `~/Documents/fusion_command.txt` ファイルの変更を監視します。
3.  **コマンド実行**: 外部プロセスがこのファイルにJSONコマンドを書き込むと、アドインがそれを検知して読み込み、対応するFusion の機能を実行します。
4.  **レスポンス返却**: 実行結果（成功、失敗、戻り値など）が `~/Documents/fusion_response.txt` にJSON形式で書き込まれます。

このAddinは、Claude Desktop 内で動作する[Claude Mcp サーバー Fusion MCP Server for Claude Desktop](<https://github.com/tomo1230/claude_fusion_mcp_server>)と連携して機能します。

---

## 主な機能

### プリミティブ形状の作成
-   直方体 (`create_box`)
-   立方体 (`create_cube`)
-   円柱 (`create_cylinder`)
-   球 (`create_sphere`)
-   半球 (`create_hemisphere`)
-   円錐 (`create_cone`)
-   多角柱 (`create_polygon_prism`)
-   トーラス (`create_torus`, `create_half_torus`)
-   パイプ (`create_pipe`)

### 高度なモデリング
-   **スイープ**: 円形パスに沿って多角形プロファイルをスイープし、ねじりを加えることが可能 (`create_polygon_sweep`)
-   **パターン**: 円形状 (`create_circular_pattern`) および矩形状 (`create_rectangular_pattern`) のパターンを作成
-   **ミラー**: 指定した平面を基準にボディを対称コピー (`copy_body_symmetric`)
-   **ブーリアン演算**: 結合、切り取り、交差 (`combine_by_name`, `combine_selection`)
-   **ディテール追加**: フィレット (`add_fillet`)、面取り (`add_chamfer`)

### ボディの操作と制御
-   **移動**: 指定した距離だけボディを移動 (`move_by_name`)
-   **回転**: 指定した軸周りにボディを回転 (`rotate_by_name`)
-   **表示/非表示**: ボディの可視性を制御 (`show_body`, `hide_body`)
-   **選択**: 名前でボディを選択 (`select_body`, `select_bodies`)

### モデル情報の取得
-   **バウンディングボックス**: ボディの寸法と境界座標を取得 (`get_bounding_box`)
-   **中心座標**: 幾何学的中心や重心を取得 (`get_body_center`)
-   **詳細寸法**: 長さ、幅、高さ、体積、表面積を取得 (`get_body_dimensions`)
-   **ジオメトリ情報**: ボディを構成する面 (`get_faces_info`) やエッジ (`get_edges_info`) の詳細情報を取得
-   **質量特性**: 体積、質量、慣性モーメントを計算 (`get_mass_properties`)
-   **ボディ間関係**: 2つのボディ間の距離、干渉、相対位置を測定 (`get_body_relationships`, `measure_distance`)

### ユーティリティ
-   **デバッグ**: Fusion の座標系情報やボディの配置情報を確認 (`debug_coordinate_info`, `debug_body_placement`)
-   **マクロ実行**: 複数のコマンドを一度にまとめて実行 (`execute_macro`)

---

## インストール方法

1.  **Add-Insフォルダを開く**
    -   Fusion で、「ユーティリティ」タブ > 「アドイン」 > 「アドイン」スクリプトとアドインをクリックします。
    -   「マイ アドイン」の横にある緑色の「+」アイコンにカーソルを合わせると、フォルダパスが表示されます。そのパスに移動してください。

2.  **ファイルの配置**
    -   このリポジトリの `fusion_mcp_server.py`を含むすべてのファイルとフォルダをクローン（またはダウンロード）します。
    ```bash
    git clone https://github.com/tomo1230/fusion_mcp_server
    ```

3.  **アドイン用フォルダ**
    -   `fusion_mcp_server` の名前でフォルダが作成されます。
    
4.  **Fusion でアドインを再読み込み**
    -   Fusion のアドインダイアログに戻り、「マイ アドイン」リストに「fusion_mcp_server」が表示されていることを確認します。
    -   必要であれば、ダイアログを一度閉じて再度開くとリストが更新されます。
    -   実行状態にします。
      
　　　<img width="581" height="211" alt="スクリーンショット 2025-08-19 234127" src="https://github.com/user-attachments/assets/34f63641-8fa6-4697-9ff1-74aff5ce8954" />

---

## 使用方法

1.  **サーバーの起動**
    -   「デザイン」ワークスペースのユーティリティタブに移動します。
    -   ツールバーに「MCPサーバー連携」という新しいパネルが表示されます。
    -   **「連携開始」** ボタンをクリックします。「MCPサーバー連携を開始しました。」というメッセージが表示されれば成功です。
    -   停止するには、**「連携停止」** ボタンをクリックします。
      
　　　<img width="284" height="134" alt="スクリーンショット 2025-08-19 233920" src="https://github.com/user-attachments/assets/394d30a5-f547-41c1-90ab-815ac64efb1b" />

2.  **コマンドの送信**
    -   任意のテキストエディタやプログラムを使い、`~/Documents/fusion_command.txt` を開きます。
    -   実行したいコマンドをJSON形式で書き込み、ファイルを保存します。

    **例1: シンプルな立方体の作成**
    ```json
    {
        "command": "create_cube",
        "parameters": {
            "size": 50,
            "body_name": "MyCube"
        }
    }
    ```

    **例2: 指定位置にテーパー付きの円柱を作成**
    ```json
    {
        "command": "create_cylinder",
        "parameters": {
            "radius": 20,
            "height": 100,
            "body_name": "TaperedCylinder",
            "cx": 50,
            "cy": 50,
            "cz": 0,
            "z_placement": "bottom",
            "taper_angle": -10
        }
    }
    ```

3.  **結果の確認**
    -   コマンドが実行されると、`~/Documents/fusion_response.txt` に結果が書き込まれます。

    **成功時のレスポンス例:**
    ```json
    {
        "status": "success",
        "result": "MyCube"
    }
    ```
    **情報取得時のレスポンス例 (`get_body_dimensions`):**
    ```json
    {
        "status": "success",
        "result": {
            "length": 50.0,
            "width": 50.0,
            "height": 50.0,
            "volume": 125000.0,
            "surface_area": 15000.0
        }
    }
    ```
    **エラー時のレスポンス例:**
    ```json
    {
        "status": "error",
        "message": "Failed to execute 'add_fillet': ボディ 'InvalidBodyName' が見つかりません。",
        "traceback": "..."
    }
    ```

4.  **サーバーの停止**
    -   ツールバーの **「連携停止」** ボタンをクリックして、ファイル監視を終了します。

---

## APIリファレンス (主要コマンド)

すべてのコマンドは `command` と `parameters` を持つJSONオブジェクトで呼び出します。単位はミリメートル(mm)です。

| コマンド | 説明 | 主要なパラメータ |
| :--- | :--- | :--- |
| **`create_box`** | 直方体を作成 | `width`, `depth`, `height`, `body_name`, `cx`, `cy`, `cz`, `z_placement` |
| **`create_cylinder`** | 円柱を作成 | `radius`, `height`, `body_name`, `cx`, `cy`, `cz`, `taper_angle` |
| **`create_sphere`** | 球を作成 | `radius`, `body_name`, `cx`, `cy`, `cz` |
| **`create_polygon_sweep`** | ねじれた多角形リングを作成 | `path_radius`, `profile_radius`, `profile_sides`, `twist_rotations`, `body_name` |
| **`add_fillet`** | ボディのエッジにフィレットを追加 | `body_name`, `radius`, `edge_indices` (省略可) |
| **`add_chamfer`** | ボディのエッジに面取りを追加 | `body_name`, `distance`, `edge_indices` (省略可) |
| **`combine_by_name`** | 2つのボディをブーリアン演算 | `target_body`, `tool_body`, `operation` ('join', 'cut', 'intersect'), `new_body_name` |
| **`move_by_name`** | ボディを相対的に移動 | `body_name`, `x_dist`, `y_dist`, `z_dist` |
| **`rotate_by_name`** | ボディを回転 | `body_name`, `axis` ('x', 'y', 'z'), `angle` (度), `cx`, `cy`, `cz` (回転中心) |
| **`create_circular_pattern`** | 円形状にボディを複製 | `source_body_name`, `axis`, `quantity`, `angle` |
| **`get_bounding_box`** | ボディのバウンディングボックスを取得 | `body_name` |
| **`get_mass_properties`** | ボディの質量特性を取得 | `body_name`, `material_density` (g/cm³) |
| **`measure_distance`** | 2ボディ間の距離を測定 | `body_name1`, `body_name2` |

---

## 使用例

**YouTube モデるんですAI チャンネル**

「しゃべるだけで、世界がカタチになる。」
ことばが、モノになる時代。
『ModerundesuAI』は、AIと会話するだけで3Dモデリングができる、
未来のモノづくり体験をシェアするYouTubeチャンネルです。
Fusion 360やBlenderなどのCADソフトとAI（ChatGPTやClaude）を連携させて、
プロンプト（命令文）でリアルな“カタチ”を自動生成。
初心者からモデリング好きまで、誰でも「つくる楽しさ」に触れられるコンテンツを発信します！

**https://www.youtube.com/@ModerundesuAI**

**「サイコロを設計して」Claude AI＆Autodesk Fusion API 連携🤖AIモデリングチャレンジ！💪**
[![](https://github.com/user-attachments/assets/c5be6840-3321-4431-8342-8ce050bc5314)](https://youtu.be/S_-xYwK5HUc?si=JWE3yv5mxRLGJaXd)

**「400mlのコップを設計して」Claude AI＆Autodesk Fusion API 連携🤖AIモデリングチャレンジ！💪**
[![](https://github.com/user-attachments/assets/820652c7-1199-4ed2-9589-4fc2b1df5a98)](https://youtu.be/abfEWtMKRV4?si=gTVDwvkIkyt81jnb)

**「使えるコマンドのテストをして」Claude AI MCP ＆ Autodesk Fusion API 連携🤖AIモデリングチャレンジ！💪**
[![](https://github.com/user-attachments/assets/aded31be-f6b3-45bb-9461-f1cd3c40ca85)](https://youtu.be/Qn-Skeh3o2c?si=7xKrM_bA7IbXT47-)

---

## 🟢 できること
- **基本形状作成** - 立方体、円柱、球など10種類の基本形状の組み合わせ
- **編集操作** - フィレット、面取り、移動、回転
- **パターン作成** - 円形・矩形配列、対称コピー
- **ブール演算** - 結合、切除、交差
- **情報取得** - 寸法、体積、質量特性の測定

## 🔴 できないこと
- **スケッチ** - 2D図形の自由描画
- **複雑形状** - 自由曲面、有機的な形状
- **アセンブリ** - 複数部品の組み立て
- **解析・製造** - CAM、FEA、レンダリング

---

## ライセンス条項


本ソフトウェアおよびそのソースコードは、著作権者が所有権を有する専有資産であり、著作権法および関連する国際条約によって保護されています。

著作権者の書面による事前の明示的な許可がない限り、本ソースコードの全部または一部を、複製、改変、翻案、結合、サブライセンス、頒布、リバースエンジニアリング、逆コンパイル、または逆アセンブルする行為は、その方法や形態を問わず一切禁じられています。本書で明示的に許諾されていない全ての権利は、著作権者に留保されます。
