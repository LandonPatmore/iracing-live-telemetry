// source: viewer/viewer_stream.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = (function() {
  if (this) { return this; }
  if (typeof window !== 'undefined') { return window; }
  if (typeof global !== 'undefined') { return global; }
  if (typeof self !== 'undefined') { return self; }
  return Function('return this')();
}.call(null));

var logger_logger_stream_pb = require('../logger/logger_stream_pb.js');
goog.object.extend(proto, logger_logger_stream_pb);
goog.exportSymbol('proto.com.landonpatmore.models.viewer.stream.CarStream', null, global);
goog.exportSymbol('proto.com.landonpatmore.models.viewer.stream.CompetitorStream', null, global);
goog.exportSymbol('proto.com.landonpatmore.models.viewer.stream.InfoStream', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.com.landonpatmore.models.viewer.stream.CarStream = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.com.landonpatmore.models.viewer.stream.CarStream, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.com.landonpatmore.models.viewer.stream.CarStream.displayName = 'proto.com.landonpatmore.models.viewer.stream.CarStream';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.com.landonpatmore.models.viewer.stream.CompetitorStream, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.com.landonpatmore.models.viewer.stream.CompetitorStream.displayName = 'proto.com.landonpatmore.models.viewer.stream.CompetitorStream';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.com.landonpatmore.models.viewer.stream.InfoStream.repeatedFields_, null);
};
goog.inherits(proto.com.landonpatmore.models.viewer.stream.InfoStream, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.com.landonpatmore.models.viewer.stream.InfoStream.displayName = 'proto.com.landonpatmore.models.viewer.stream.InfoStream';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.toObject = function(opt_includeInstance) {
  return proto.com.landonpatmore.models.viewer.stream.CarStream.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.com.landonpatmore.models.viewer.stream.CarStream} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.toObject = function(includeInstance, msg) {
  var f, obj = {
    fuellevel: jspb.Message.getFloatingPointFieldWithDefault(msg, 1, 0.0),
    fuelpercentage: jspb.Message.getFloatingPointFieldWithDefault(msg, 2, 0.0),
    fueluseperhour: jspb.Message.getFloatingPointFieldWithDefault(msg, 3, 0.0),
    flagstatus: jspb.Message.getFieldWithDefault(msg, 4, 0),
    enginewarnings: jspb.Message.getFieldWithDefault(msg, 5, 0),
    carsinproximity: jspb.Message.getFieldWithDefault(msg, 6, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.com.landonpatmore.models.viewer.stream.CarStream;
  return proto.com.landonpatmore.models.viewer.stream.CarStream.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.com.landonpatmore.models.viewer.stream.CarStream} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setFuellevel(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setFuelpercentage(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setFueluseperhour(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setFlagstatus(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setEnginewarnings(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setCarsinproximity(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.com.landonpatmore.models.viewer.stream.CarStream.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.com.landonpatmore.models.viewer.stream.CarStream} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = /** @type {number} */ (jspb.Message.getField(message, 1));
  if (f != null) {
    writer.writeFloat(
      1,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 2));
  if (f != null) {
    writer.writeFloat(
      2,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 3));
  if (f != null) {
    writer.writeFloat(
      3,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 4));
  if (f != null) {
    writer.writeInt32(
      4,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 5));
  if (f != null) {
    writer.writeInt32(
      5,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 6));
  if (f != null) {
    writer.writeInt32(
      6,
      f
    );
  }
};


/**
 * optional float fuelLevel = 1;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getFuellevel = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 1, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setFuellevel = function(value) {
  return jspb.Message.setField(this, 1, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearFuellevel = function() {
  return jspb.Message.setField(this, 1, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasFuellevel = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional float fuelPercentage = 2;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getFuelpercentage = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 2, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setFuelpercentage = function(value) {
  return jspb.Message.setField(this, 2, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearFuelpercentage = function() {
  return jspb.Message.setField(this, 2, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasFuelpercentage = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional float fuelUsePerHour = 3;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getFueluseperhour = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 3, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setFueluseperhour = function(value) {
  return jspb.Message.setField(this, 3, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearFueluseperhour = function() {
  return jspb.Message.setField(this, 3, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasFueluseperhour = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional int32 flagStatus = 4;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getFlagstatus = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setFlagstatus = function(value) {
  return jspb.Message.setField(this, 4, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearFlagstatus = function() {
  return jspb.Message.setField(this, 4, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasFlagstatus = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional int32 engineWarnings = 5;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getEnginewarnings = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 5, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setEnginewarnings = function(value) {
  return jspb.Message.setField(this, 5, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearEnginewarnings = function() {
  return jspb.Message.setField(this, 5, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasEnginewarnings = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional int32 carsInProximity = 6;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.getCarsinproximity = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.setCarsinproximity = function(value) {
  return jspb.Message.setField(this, 6, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CarStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.clearCarsinproximity = function() {
  return jspb.Message.setField(this, 6, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CarStream.prototype.hasCarsinproximity = function() {
  return jspb.Message.getField(this, 6) != null;
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.toObject = function(opt_includeInstance) {
  return proto.com.landonpatmore.models.viewer.stream.CompetitorStream.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.toObject = function(includeInstance, msg) {
  var f, obj = {
    caridx: jspb.Message.getFieldWithDefault(msg, 1, 0),
    carclassposition: jspb.Message.getFieldWithDefault(msg, 2, 0),
    percentagearoundtrack: jspb.Message.getFloatingPointFieldWithDefault(msg, 3, 0.0),
    onpitroad: jspb.Message.getBooleanFieldWithDefault(msg, 4, false),
    position: jspb.Message.getFieldWithDefault(msg, 5, 0),
    trackstatus: jspb.Message.getFieldWithDefault(msg, 6, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.com.landonpatmore.models.viewer.stream.CompetitorStream;
  return proto.com.landonpatmore.models.viewer.stream.CompetitorStream.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setCaridx(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setCarclassposition(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setPercentagearoundtrack(value);
      break;
    case 4:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setOnpitroad(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setPosition(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setTrackstatus(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.com.landonpatmore.models.viewer.stream.CompetitorStream.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = /** @type {number} */ (jspb.Message.getField(message, 1));
  if (f != null) {
    writer.writeInt32(
      1,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 2));
  if (f != null) {
    writer.writeInt32(
      2,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 3));
  if (f != null) {
    writer.writeFloat(
      3,
      f
    );
  }
  f = /** @type {boolean} */ (jspb.Message.getField(message, 4));
  if (f != null) {
    writer.writeBool(
      4,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 5));
  if (f != null) {
    writer.writeInt32(
      5,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 6));
  if (f != null) {
    writer.writeInt32(
      6,
      f
    );
  }
};


/**
 * optional int32 carIdx = 1;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getCaridx = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setCaridx = function(value) {
  return jspb.Message.setField(this, 1, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearCaridx = function() {
  return jspb.Message.setField(this, 1, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasCaridx = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional int32 carClassPosition = 2;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getCarclassposition = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setCarclassposition = function(value) {
  return jspb.Message.setField(this, 2, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearCarclassposition = function() {
  return jspb.Message.setField(this, 2, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasCarclassposition = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional float percentageAroundTrack = 3;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getPercentagearoundtrack = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 3, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setPercentagearoundtrack = function(value) {
  return jspb.Message.setField(this, 3, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearPercentagearoundtrack = function() {
  return jspb.Message.setField(this, 3, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasPercentagearoundtrack = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional bool onPitRoad = 4;
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getOnpitroad = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 4, false));
};


/**
 * @param {boolean} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setOnpitroad = function(value) {
  return jspb.Message.setField(this, 4, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearOnpitroad = function() {
  return jspb.Message.setField(this, 4, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasOnpitroad = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional int32 position = 5;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getPosition = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 5, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setPosition = function(value) {
  return jspb.Message.setField(this, 5, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearPosition = function() {
  return jspb.Message.setField(this, 5, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasPosition = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional int32 trackStatus = 6;
 * @return {number}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.getTrackstatus = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/**
 * @param {number} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.setTrackstatus = function(value) {
  return jspb.Message.setField(this, 6, value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.clearTrackstatus = function() {
  return jspb.Message.setField(this, 6, undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.CompetitorStream.prototype.hasTrackstatus = function() {
  return jspb.Message.getField(this, 6) != null;
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.repeatedFields_ = [4];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.toObject = function(opt_includeInstance) {
  return proto.com.landonpatmore.models.viewer.stream.InfoStream.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.com.landonpatmore.models.viewer.stream.InfoStream} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.toObject = function(includeInstance, msg) {
  var f, obj = {
    car: (f = msg.getCar()) && proto.com.landonpatmore.models.viewer.stream.CarStream.toObject(includeInstance, f),
    weather: (f = msg.getWeather()) && logger_logger_stream_pb.LoggerWeather.toObject(includeInstance, f),
    session: (f = msg.getSession()) && logger_logger_stream_pb.LoggerSession.toObject(includeInstance, f),
    competitorsList: jspb.Message.toObjectList(msg.getCompetitorsList(),
    proto.com.landonpatmore.models.viewer.stream.CompetitorStream.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.com.landonpatmore.models.viewer.stream.InfoStream;
  return proto.com.landonpatmore.models.viewer.stream.InfoStream.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.com.landonpatmore.models.viewer.stream.InfoStream} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.com.landonpatmore.models.viewer.stream.CarStream;
      reader.readMessage(value,proto.com.landonpatmore.models.viewer.stream.CarStream.deserializeBinaryFromReader);
      msg.setCar(value);
      break;
    case 2:
      var value = new logger_logger_stream_pb.LoggerWeather;
      reader.readMessage(value,logger_logger_stream_pb.LoggerWeather.deserializeBinaryFromReader);
      msg.setWeather(value);
      break;
    case 3:
      var value = new logger_logger_stream_pb.LoggerSession;
      reader.readMessage(value,logger_logger_stream_pb.LoggerSession.deserializeBinaryFromReader);
      msg.setSession(value);
      break;
    case 4:
      var value = new proto.com.landonpatmore.models.viewer.stream.CompetitorStream;
      reader.readMessage(value,proto.com.landonpatmore.models.viewer.stream.CompetitorStream.deserializeBinaryFromReader);
      msg.addCompetitors(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.com.landonpatmore.models.viewer.stream.InfoStream.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.com.landonpatmore.models.viewer.stream.InfoStream} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCar();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.com.landonpatmore.models.viewer.stream.CarStream.serializeBinaryToWriter
    );
  }
  f = message.getWeather();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      logger_logger_stream_pb.LoggerWeather.serializeBinaryToWriter
    );
  }
  f = message.getSession();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      logger_logger_stream_pb.LoggerSession.serializeBinaryToWriter
    );
  }
  f = message.getCompetitorsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      4,
      f,
      proto.com.landonpatmore.models.viewer.stream.CompetitorStream.serializeBinaryToWriter
    );
  }
};


/**
 * optional CarStream car = 1;
 * @return {?proto.com.landonpatmore.models.viewer.stream.CarStream}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.getCar = function() {
  return /** @type{?proto.com.landonpatmore.models.viewer.stream.CarStream} */ (
    jspb.Message.getWrapperField(this, proto.com.landonpatmore.models.viewer.stream.CarStream, 1));
};


/**
 * @param {?proto.com.landonpatmore.models.viewer.stream.CarStream|undefined} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
*/
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.setCar = function(value) {
  return jspb.Message.setWrapperField(this, 1, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.clearCar = function() {
  return this.setCar(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.hasCar = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional com.landonpatmore.models.logger.LoggerWeather weather = 2;
 * @return {?proto.com.landonpatmore.models.logger.LoggerWeather}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.getWeather = function() {
  return /** @type{?proto.com.landonpatmore.models.logger.LoggerWeather} */ (
    jspb.Message.getWrapperField(this, logger_logger_stream_pb.LoggerWeather, 2));
};


/**
 * @param {?proto.com.landonpatmore.models.logger.LoggerWeather|undefined} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
*/
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.setWeather = function(value) {
  return jspb.Message.setWrapperField(this, 2, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.clearWeather = function() {
  return this.setWeather(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.hasWeather = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional com.landonpatmore.models.logger.LoggerSession session = 3;
 * @return {?proto.com.landonpatmore.models.logger.LoggerSession}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.getSession = function() {
  return /** @type{?proto.com.landonpatmore.models.logger.LoggerSession} */ (
    jspb.Message.getWrapperField(this, logger_logger_stream_pb.LoggerSession, 3));
};


/**
 * @param {?proto.com.landonpatmore.models.logger.LoggerSession|undefined} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
*/
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.setSession = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.clearSession = function() {
  return this.setSession(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.hasSession = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * repeated CompetitorStream competitors = 4;
 * @return {!Array<!proto.com.landonpatmore.models.viewer.stream.CompetitorStream>}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.getCompetitorsList = function() {
  return /** @type{!Array<!proto.com.landonpatmore.models.viewer.stream.CompetitorStream>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.com.landonpatmore.models.viewer.stream.CompetitorStream, 4));
};


/**
 * @param {!Array<!proto.com.landonpatmore.models.viewer.stream.CompetitorStream>} value
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
*/
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.setCompetitorsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 4, value);
};


/**
 * @param {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream=} opt_value
 * @param {number=} opt_index
 * @return {!proto.com.landonpatmore.models.viewer.stream.CompetitorStream}
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.addCompetitors = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 4, opt_value, proto.com.landonpatmore.models.viewer.stream.CompetitorStream, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.com.landonpatmore.models.viewer.stream.InfoStream} returns this
 */
proto.com.landonpatmore.models.viewer.stream.InfoStream.prototype.clearCompetitorsList = function() {
  return this.setCompetitorsList([]);
};


goog.object.extend(exports, proto.com.landonpatmore.models.viewer.stream);
