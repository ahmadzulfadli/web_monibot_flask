from dbClass import *
# read---------------------------------------------------------


@app.route('/')
def index():
    # menampilkan data terbaru
    dataMonibot = Monibot.query.order_by(
        Monibot.timestamp.desc()).first()
    
    #menghitung jumlah data
    count_data = Monibot.query.count()

    # fluktuasi data sensor
    # sensor temperature
    if count_data > 0:
        lastTemperature = Monibot.query.order_by(
            Monibot.timestamp.desc()).first().data_temp
        lastHumidity = Monibot.query.order_by(
            Monibot.timestamp.desc()).first().data_humd
        lastPpmch4 = Monibot.query.order_by(
            Monibot.timestamp.desc()).first().data_ppmch4
        lastPpmco = Monibot.query.order_by(
            Monibot.timestamp.desc()).first().data_ppmco

        # fluktuasi data sensor
        fluktuasi = {
            'temperature': lastTemperature,
            'humidity': lastHumidity,
            'ppmch4': lastPpmch4,
            'ppmco': lastPpmco
        }
    else:
        fluktuasi = {
            'temperature': 0,
            'humidity': 0,
            'ppmch4': 0,
            'ppmco': 0
        }

    # menampilkan 5 data terbaru
    lastdata = Monibot.query.order_by(
        Monibot.timestamp.desc()).limit(5).all()

    # menampilkan 9 data terbaru
    grafikMonibot = Monibot.query.order_by(
        Monibot.timestamp.desc()).limit(10).all()

    # Konversi data menjadi format JSON
    grafik_json = []
    for item in grafikMonibot:
        grafik_json.append({
            'label': item.timestamp.strftime('%H:%M'),
            'temperature': item.data_temp,
            'humidity': item.data_humd,
            'ppmch4': item.data_ppmch4,
            'ppmco': item.data_ppmco,            
        })

    return render_template('index.html', data=dataMonibot, grafik=grafik_json, lastdata=lastdata, fluktuasi=fluktuasi)


@app.route('/tabel')
def tabel():
    # menampilkan data dari yang terbaru
    dataMonibot = dataMonibot = Monibot.query.order_by(
        Monibot.timestamp.desc()).all()

    return render_template('tabel.html', data=dataMonibot)


@app.route('/device')
def device():
    return render_template('device.html')

# create-------------------------------------------------------


# @app.route('/inputData', methods=['GET'])
# def inputData():
#     try:
#         mode = request.args.get('mode')
#         if mode != 'save':
#             return jsonify({"error": "Mode not found."}), 400

#         else:
#             temperature = request.args.get('temperature', type=float)
#             moisture = request.args.get('moisture', type=float)
#             ph_meter = request.args.get('ph_meter', type=float)
#             count_day = request.args.get('count_day', type=int)

#             if temperature is None or moisture is None or ph_meter is None or count_day is None:
#                 return jsonify({"error": "Temperature or moisture or ph_meter or count_day parameters are required."}), 400

#             # Lakukan operasi simpan data ke database atau lakukan tindakan sesuai kebutuhan
#             newMonibot = Monibot(
#                 temperature=temperature,
#                 moisture=moisture,
#                 ph_meter=ph_meter,
#                 count_day=count_day,
#             )

#             # Tambahkan data baru ke session
#             db.session.add(newMonibot)
#             # Commit session untuk menyimpan perubahan data ke database
#             db.session.commit()

#             return redirect(url_for('lihatData'))

#     except Exception as e:
#         return jsonify({"error": "An error occurred while trying to add sensor data."}), 500


# @app.route('/lihatData', methods=['GET'])
# def lihatData():
#     # tampilkan seluruh database dalam format json
#     dataMonibot = Monibot.query.order_by(
#         Monibot.timestamp.desc()).all()
#     data = []
#     for item in dataMonibot:
#         data.append({
#             'id': item.id,
#             'temperature': item.temperature,
#             'moisture': item.moisture,
#             'ph_meter': item.ph_meter,
#             'count_day': item.count_day,
#             'timestamp': item.timestamp.strftime('%H:%M'),
#         })

#     response = {
#         "status": "success",
#         "message": "Sensor data added successfully!",
#         "data": data
#     }

#     return jsonify(response), 200


if __name__ == '__main__':
    # Launch the application
    app.run(port=8000, debug=True)