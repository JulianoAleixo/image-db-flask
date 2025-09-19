from flask import Blueprint, request, jsonify
from app.models.image_model import ImageModel
import base64

image_bp = Blueprint('images', __name__)

# CREATE
@image_bp.route('', methods=['POST'])
def upload_image():
    """
    Recebe uma imagem (multipart/form-data) e salva no Firestore.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    filename = file.filename
    file_bytes = file.read()
    encoded_string = base64.b64encode(file_bytes).decode('utf-8')

    doc_id = ImageModel.create(filename, encoded_string)
    return jsonify({'message': 'Imagem salva com sucesso!', 'id': doc_id}), 201

# READ ALL
@image_bp.route('', methods=['GET'])
def list_images():
    images = ImageModel.get_all()
    return jsonify(images), 200

# READ ONE
@image_bp.route('/<id>', methods=['GET'])
def get_image(id):
    image = ImageModel.get_by_id(id)
    if not image:
        return jsonify({'error': 'Imagem não encontrada'}), 404
    return jsonify(image), 200

# UPDATE
@image_bp.route('/<id>', methods=['PUT'])
def update_image(id):
    """
    Atualiza filename ou imagem Base64.
    Pode enviar um novo arquivo em 'file' ou apenas 'filename'.
    """
    filename = request.form.get('filename')
    imageBase64 = None

    if 'file' in request.files:
        file = request.files['file']
        file_bytes = file.read()
        imageBase64 = base64.b64encode(file_bytes).decode('utf-8')

    updated = ImageModel.update(id, filename, imageBase64)
    if not updated:
        return jsonify({'error': 'Nada para atualizar'}), 400

    return jsonify({'message': 'Imagem atualizada com sucesso'}), 200

# DELETE
@image_bp.route('/<id>', methods=['DELETE'])
def delete_image(id):
    image = ImageModel.get_by_id(id)
    if not image:
        return jsonify({'error': 'Imagem não encontrada'}), 404

    ImageModel.delete(id)
    return jsonify({'message': 'Imagem deletada com sucesso'}), 200
