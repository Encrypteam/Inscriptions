from flask import Blueprint, request, jsonify
from main import db
from main.models import Inscription
from main.blockchain.algorand import send_algorand_txn, sign_algorand_txn, create_algorand_txn

routes = Blueprint('inscription_controller', __name__)

@routes.route('/inscribir', methods=['POST'])
def inscribir():
    data = request.json
    user_name = data['user_name']
    user_lastname = data['user_lastname']
    dni = data['dni']
    subject = data['subject']

    sender_address = "CX3GAT3JEU4QNASFFSQYBASP6FO56OBZIW4IB57PB35DFNL6POD5SZC4CE"
    recipient_address = "CC6UUZ7JLDVUJDN22MYWEWTSAHI3B7KESPOVUKOKVYNG4EKNO2KDIDLKFY"

    # Crear la transacción en Algorand
    txn = create_algorand_txn(sender_address, recipient_address)

    # Firmar la transacción
    sender_mnemonic = "thought dwarf cheap response captain own theme upper case trip auction game result ring employ wrist draw nut number blue total confirm duty abandon minute"  # Reemplaza con tu mnemónico
    signed_txn = sign_algorand_txn(txn, sender_mnemonic)

    # Enviar la transacción a Algorand
    txid = send_algorand_txn(signed_txn)

    # Guardar la inscripción en la base de datos junto con el ID de transacción
    inscripcion = Inscription(
        user_name=user_name,
        user_lastname=user_lastname,
        dni=dni,
        subject=subject,
        trasaction_id=txid
    )

    db.session.add(inscripcion)
    db.session.commit()
    return jsonify({
        'message': 'Inscripción exitosa',
        'user_name': user_name,
        'user_lastname': user_lastname,
        'dni': dni,
        'subject': subject,
        'transaction_id': txid
    })

